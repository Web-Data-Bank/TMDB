folder="/content/TMDB/json"

count=0

# Loop through the files in the folder
for file in "$folder"/*
do
  if (count % 500 != 0); then
    echo "$file"
    mv $file /content/TMDB-1/json/
    rm $file
    count=$((count+1))
  else
    git add -A --verbose
    git commit -m "Move"
    git push
  fi
  
done
