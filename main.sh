for (( i = 950000; i < 1000000; i = i + 10000))
do 
    echo $i
    python3 app.py "$i"
    git add -A --verbose
    git commit -m "$i"
    git push
done
