python3 main.py
for (( i = 0; i < 50000; i = i + 1000))
do 
    echo $FILE
    python3 code.py "$i"
    git add -A --verbose
    git commit -m "$i"
    git push
    rm $FILE
done