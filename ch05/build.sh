#!/bin/sh
# Build script for ch05

curl https://nlp100.github.io/data/ai.ja.zip -o /usr/local/nlp/ch05/ai.ja.zip
unzip /usr/local/nlp/ch05/ai.ja.zip -d /usr/local/nlp/ch05/

# Install CRF++
wget "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7QVR6VXJ5dWExSTQ" -O /usr/local/nlp/ch05/CRF++-0.58.tar.gz
cd /usr/local/nlp/ch05/
tar -zxvf ./CRF++-0.58.tar.gz
cd /usr/local/nlp/ch05/CRF++-0.58
./configure --build=arm-unknown-linux-gnu --host=arm-unknown-linux-gnu --target=arm-unknown-linux-gnu
make
make install
echo "/usr/local/lib" >> /etc/ld.so.conf
echo "/usr/local/lib" >> /etc/ld.so.conf.d/lib.conf
ldconfig

# Install CaboCha
cd /usr/local/nlp/ch05/
FILE_ID=0B4y35FiV1wh7SDd1Q1dUQkZQaUU
FILE_NAME=cabocha-0.69.tar.bz2
curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${FILE_ID}" > /dev/null
CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=${FILE_ID}" -o ${FILE_NAME}
tar -jxvf ${FILE_NAME}
cd /usr/local/nlp/ch05/cabocha-0.69
./configure --build=arm-unknown-linux-gnu --host=arm-unknown-linux-gnu --target=arm-unknown-linux-gnu --with-charset=UTF8
make
make install

touch  /usr/local/lib/cabocha/model/charset-file.txt
echo "UTF-8" >  /usr/local/lib/cabocha/model/charset-file.txt
sed -i 's/^# charset-file/charset-file/' /usr/local/etc/cabocharc
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
cd /usr/local/nlp/ch05/cabocha-0.69/python
python setup.py install

cd /usr/local/nlp/ch05/
ln -s ../ch04/tokenizer.py ./tokenizer.py
