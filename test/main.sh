git config --global pack.threads "8"
for (( i = 187; i >= 100; i--))
do 
    # rm json/$i.json
    echo $i
    python3 main.py "$i"
    git add -A --verbose
    git commit -m "Added alternative_title $i"
    git push
done