#!/bin/bash

base_path=$(cd `dirname $0`; pwd)

cd ${base_path}
current_version=`cat ${base_path}/current_version`
pwd
rm -vfr ${base_path}/build ${base_path}/dist
sed "s/0.0.{current_version}/0.0.$(( current_version + 1 ))/g" setup_template.py > setup.py

cat setup.py

python setup.py bdist_wheel --universal && twine upload ${base_path}//dist/*

echo $(( current_version + 1 )) > ${base_path}/current_version