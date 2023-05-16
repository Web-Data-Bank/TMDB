for (( i = 200000; i < 250000; i = i + 250))
do 
    echo $i
    python3 app.py "$i"
    git add -A --verbose
    git commit -m "$i"
    git push
done
