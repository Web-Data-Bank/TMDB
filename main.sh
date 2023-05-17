for (( i = 99000; i <= 100000; i = i + 250))
do 
    rm json/$i.json
    # echo $i
    # python3 app.py "$i"
    # git add -A --verbose
    # git commit -m "$i"
    # git push
done