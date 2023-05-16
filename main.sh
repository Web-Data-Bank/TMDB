for (( i = 300000; i < 350000; i = i + 500))
do 
    echo $i
    python3 app.py "$i"
    git add -A --verbose
    git commit -m "$i"
    git push
done
