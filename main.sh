git config --global pack.threads "8"
for (( i = 450000; i < 500000; i = i + 10/00))
do 
    echo $i
    python3 app.py "$i"
    git add -A --verbose
    git commit -m "$i"
    git push
done
