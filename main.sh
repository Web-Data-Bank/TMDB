for (( i = 600000; i < 750000; i = i + 10000))
do 
    echo $i
    python3 app.py "$i"
    git add -A --verbose
    git commit -m "$i"
    git push
done
