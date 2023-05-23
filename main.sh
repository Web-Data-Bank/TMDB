for (( i = 571346; i < 600000; i = i + 1000))
do 
    echo $i
    python3 app.py "$i"
    git add -A --verbose
    git commit -m "$i"
    git push
done
