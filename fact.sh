echo "enter the number"
read a
f=1
i=0
while [ $i -ne $a ] 
do
i=`expr $i + 1`
f=`expr $f \* $i`
done
echo "factorial is $f"
