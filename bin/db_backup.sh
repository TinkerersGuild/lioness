echo $LIONESS
mysqldump --defaults-file=$LIONESS/mysql.cred lioness > docs/lioness_bup.sql
