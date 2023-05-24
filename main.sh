for (( i = 1100000; i < 1131071; i = i + 5000))
do 
    echo $i
    python3 app.py "$i"
    git add -A --verbose
    git commit -m "$i"
    git push
done
