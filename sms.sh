#!/bin/bash
#TLEGRAM:i4m_mrx
clear



echo -e " -\e[92m(COD BY MRX)\e[0m"



echo -e "\e[32mWhat do you want?\e[0m"
echo -e " 1. \e[34mSend SMS\e[0m"
echo -e " 2. \e[34mSMS Bomb / SMS Spam\e[0m"
read option

check() {
if [ $? = 0 ]; then
echo -e "\e[32mMessage successfully sent\e[0m"
elif [ $? = 1 ]; then
echo -e "\e[31mMessage sent failed. You might want to try again?\e[0m"
else
echo "Unknown error"
fi
}


if [ "$zCh" = "$Ch2" ]; then
   rm -f log

   if [ "$option" == "1" ] || [ "$option" == "a" ]; then
      while [ -z "$num" ]
      do
         echo -e "\e[31m[\e[0m\e[32mZ\e[0m\e[31m]\e[0m \e[32mEnter number\e[0m\e[34m"
         read num
      done
      while [ -z "$msg" ]
      do
         echo -e "\e[31m[\e[0m\e[32mZ\e[0m\e[31m]\e[0m \e[32mEnter Message:\e[0m\e[34m"
         read msg
      done

      termux-sms-send -n "$num" "$msg"

   elif [ "$option" == "B" ] || [ "$option" == "b" ]; then
      echo -e "\e[31m[\e[0m\e[32mZ\e[0m\e[31m]\e[0m \e[32mHow many sms you want to send? "
      read loop
      i=0
      while [ $i -lt $loop ]
      do
         while [ -z "$num" ]
         do
            echo -e "\e[31m[\e[0m\e[32mZ\e[0m\e[31m]\e[0m \e[32mEnter number(s seperated by comma e.g 09123456789,09987654321,09123498765)\e[0m\e[34m"
            read num
         done
         while [ -z "$msg" ]
         do
            echo -e "\e[31m[\e[0m\e[32mZ\e[0m\e[31m]\e[0m \e[32mEnter Message:\e[0m\e[34m"
            read msg
         done

         termux-sms-send -n "$num" "$msg"
         i=$[$i+1]
         echo -e "\e[32m$i message sent\e[0m"
      done
   else
      echo -e "\e[31mWrong input. Please enter valid choice\e[0m"
   fi

elif [ "$zCh" != "$ChB" ]; then
   echo -e "\e[91mLooks like you don't have termux-api app. Please install it first.\e[0m"
else
   echo "unknown error"
fi

rm -f log
