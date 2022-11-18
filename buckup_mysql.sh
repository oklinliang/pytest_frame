#!/bin/bash
docker exec -i mysql8 bash <<'EOF'
echo "数据库开始备份"
mysqldump -u risk_admin -h rm-2ze0k2r2a667u5i18no.mysql.rds.aliyuncs.com -p"pu5e&Z^o" --set-gtid-purged=off risk > ~/liang.sql
echo "数据库备份完成"
echo "准备同步数据库"
mysql -u root -p"tybtest" risk < ~/liang.sql
echo "数据库同步完成"
rm -f ~/liang.sql
exit
EOF
