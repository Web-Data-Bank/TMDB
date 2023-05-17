git config --global pack.threads "8"
for (( i = 500000; i < 550000; i = i + 1000))
do 
    echo $i
    python3 app.py "$i"
    git add -A --verbose
    git commit -m "$i"
    git push
done
