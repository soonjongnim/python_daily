{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['C:\\\\Users\\\\BIT-R39\\\\anaconda3\\\\envs\\\\python36\\\\lib\\\\site-packages\\\\ipykernel_launcher.py', '-f', 'C:\\\\Users\\\\BIT-R39\\\\AppData\\\\Roaming\\\\jupyter\\\\runtime\\\\kernel-5118a761-4971-44ce-a8f3-485df81d6594.json'] 3\n",
      "안녕하세요 -f\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "\n",
    "print(sys.argv, len(sys.argv))\n",
    "print('안녕하세요 {}'.format(sys.argv[1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Traceback (most recent call last):\n",
      "  File \"hello.py\", line 26, in <module>\n",
      "    \"execution_count\": null,\n",
      "NameError: name 'null' is not defined\n"
     ]
    }
   ],
   "source": [
    "!python hello.py 홍길동"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 표쥰 입력을 받을때"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " aaa\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'aaa'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "input()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
