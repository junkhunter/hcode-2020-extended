time cat a.txt | python3 rh_d_best.py > a_rep &
time cat b.txt | python3 rh_d_best.py > b_rep &
time cat c.txt | python3 rh_d_best.py > c_rep &
time cat d.txt | python3 rh_d_best.py > d_rep &
time cat e.txt | python3 rh_d_best.py > e_rep &
time cat f.txt | python3 rh_d_best.py > f_rep &

# x=6
# while [ $x != 0 ]
# do
#     fg
#     echo "$x restants"
#     x=$(( $x - 1 ))
# done