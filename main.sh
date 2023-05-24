git config --global pack.threads "8"
for (( i = 695000; i <= 750000; i = i + 5000))
do 
    # rm json/$i.json
    echo $i
    python3 app.py "$i"
    git add -A --verbose
    git commit -m "$i"
    git push
done
