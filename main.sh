git config --global pack.threads "8"
for (( i = 300000; i < 120000; i = i + 50000))
do 
    # rm json/$i.json
    echo $i
    python3 removeNonContentFiles.py "$i"
    git add -A --verbose
    git commit -m "Removed $i Unwanted JSON And Adult Flims"
    git push
done