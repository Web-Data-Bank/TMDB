for (( i = 1000000; i < 1050000; i = i + 5000))
do 
    echo $i
    python3 app.py "$i"
    git add -A --verbose
    git commit -m "$i"
    git push
done
