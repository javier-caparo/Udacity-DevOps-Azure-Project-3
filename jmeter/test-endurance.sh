#!/bin/bash
#
rootPath=$1
testFile=$2
host="jc-test-appservice.azurewebsites.net"

echo "Root path: $rootPath"
echo "Test file: $testFile"

T_DIR=.

# Reporting dir: start fresh
R_DIR=$T_DIR/endurance-report
rm -rf $R_DIR > /dev/null 2>&1
mkdir -p $R_DIR

rm -f $T_DIR/test-plan.jtl $T_DIR/jmeter.log  > /dev/null 2>&1

./run-endurance-test.sh $rootPath -Dlog_level.jmeter=DEBUG \
	-Jhost=$host \
	-n -t /test/$testFile -l $T_DIR/endurance-endurance-plan.jtl -j $T_DIR/endurance-jmeter.log \
	-e -o $R_DIR

echo "==== jmeter.log ===="
cat $T_DIR/jmeter.log

echo "==== Raw Test Report ===="
cat $T_DIR/endurance-test-plan.jtl

echo "==== HTML Test Report ===="
echo "See HTML test report in $R_DIR/index.html"