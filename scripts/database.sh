#!/bin/bash

ACTION=$1

DB=db.sqlite3
DATA=../data
TABLES=(transport_aduana transport_extraordinario transport_flete transport_gastos transport_honorarios
transport_kma transport_machine transport_puerto transport_taxcountry transport_transport transport_tsa)
DATE=$(date +%Y%m%d-%H%M%S)

cd $DATA
case $ACTION in
    export|import)
        for table in ${TABLES[@]}; do 
            file=${table}.csv
            case $ACTION in
                export)
sqlite3 -batch $DB <<EOSCRIPT
.header on
.mode csv
.once $DATA/$file
select * from $table;
EOSCRIPT
                ;;
                import)
sqlite3 -batch $DB <<EOSCRIPT
.mode csv
.import $DATA/$file
EOSCRIPT
                ;;
            esac
        done
            ;;
    backup_db)
        echo '.dump'| sqlite3 $DB | gzip -c > mercyl_${DATE}.dump.gz
    ;;
restore_db)
    zcat $RESTORE_DB | sqlite3 $DB_NAME
esac

