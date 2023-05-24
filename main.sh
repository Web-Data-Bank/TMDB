for (( i = 850000; i < 900000; i = i + 5000))
do 
    echo $i
    python3 app.py "$i"
    git add -A --verbose
    git commit -m "$i"
    git push
done
