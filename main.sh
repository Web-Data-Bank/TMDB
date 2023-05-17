git config --global pack.threads "8"
for (( i = 550000; i <= 700000; i = i + 2500))
do 
    # rm json/$i.json
    echo $i
    python3 app.py "$i"
    git add -A --verbose
    git commit -m "$i"
    git push
done
