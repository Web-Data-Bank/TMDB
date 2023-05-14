for (( i = 67000; i < 100000; i = i + 1000))
do 
    echo $i
    python3 app.py "$i"
    git add -A --verbose
    git commit -m "$i"
    git push
done
