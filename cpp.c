#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <future>
#include <curl/curl.h>

void downloadAPI(const std::string& id) {
    std::string url = "https://api.themoviedb.org/3/movie/" + id + "/alternative_titles?api_key=ed0646253701d7550481764a488b6ded";
    std::ofstream file("alternative_titles/" + id + ".json", std::ios::binary);
    if (file.is_open()) {
        CURL* curl = curl_easy_init();
        if (curl) {
            curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
            curl_easy_setopt(curl, CURLOPT_TIMEOUT, 10L);
            curl_easy_setopt(curl, CURLOPT_WRITEDATA, &file);
            curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, [](void* ptr, size_t size, size_t nmemb, void* stream) {
                size_t written = fwrite(ptr, size, nmemb, static_cast<FILE*>(stream));
                return written;
            });
            CURLcode res = curl_easy_perform(curl);
            if (res != CURLE_OK)
                std::cerr << "Failed to download: " << curl_easy_strerror(res) << '\n';
            curl_easy_cleanup(curl);
        }
        else {
            std::cerr << "Failed to initialize CURL\n";
        }
        file.close();
    }
    else {
        std::cerr << "Failed to open file for writing: " << id << ".json\n";
    }
}

int main() {
    std::string file_path = "file_names.txt";
    std::ifstream file(file_path);
    if (file.is_open()) {
        std::vector<std::string> movies_id;
        std::string line;
        while (std::getline(file, line))
            movies_id.push_back(line);

        size_t num_tasks = movies_id.size();
        std::cout << num_tasks << '\n';

        std::vector<std::future<void>> futures;
        for (const std::string& id : movies_id)
            futures.emplace_back(std::async(std::launch::async, downloadAPI, id));

        for (size_t i = 0; i < num_tasks; ++i) {
            futures[i].wait();
            std::cerr << "\rdone " << static_cast<double>(i + 1) / num_tasks * 100 << "%";
        }
        std::cerr << '\n';
    }
    else {
        std::cerr << "Failed to open file: " << file_path << '\n';
    }

    return 0;
}
