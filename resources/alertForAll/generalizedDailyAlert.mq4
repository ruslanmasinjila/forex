//+------------------------------------------------------------------+
//|                                   Indicator: Dailyrangealert.mq4 |
//|                                       Created with EABuilder.com |
//|                                             http://eabuilder.com |
//+------------------------------------------------------------------+
#property copyright "Created with EABuilder.com"
#property link      "http://eabuilder.com"
#property version   "1.00"
#property description ""

#include <stdlib.mqh>
#include <stderror.mqh>

//--- indicator settings
#property indicator_chart_window
#property indicator_buffers 1

#property indicator_type1 DRAW_ARROW
#property indicator_width1 5
#property indicator_color1 0xFF00BF
#property indicator_label1 "Alert"

#define PERIOD_M2 2
#define PERIOD_M3 3
#define PERIOD_M4 4
#define PERIOD_M6 6
#define PERIOD_M10 10
#define PERIOD_M12 12
#define PERIOD_M20 20
#define PERIOD_H2 120
#define PERIOD_H3 180
#define PERIOD_H6 360
#define PERIOD_H8 480
#define PERIOD_H12 720



string CurrPair[27]={"AUDCAD","AUDCHF","AUDJPY","AUDNZD","AUDUSD","CADCHF","CHFJPY","EURAUD","EURCAD","EURCHF","EURGBP","EURJPY","EURNZD","EURUSD","GBPAUD","GBPCAD","GBPCHF","GBPJPY","GBPNZD","GBPUSD","NZDCAD","NZDCHF","NZDJPY","NZDUSD","USDCAD","USDCHF","USDJPY"};
//string CurrPair[2]={"USDCHF","EURUSD"};
int timeFrames[21]={PERIOD_M1,PERIOD_M5,PERIOD_M15,PERIOD_M30,PERIOD_H1,PERIOD_H4,PERIOD_D1,PERIOD_W1,PERIOD_MN1,PERIOD_M2,PERIOD_M3,PERIOD_M4,PERIOD_M6,PERIOD_M10,PERIOD_M12,PERIOD_M20,PERIOD_H2,PERIOD_H3,PERIOD_H6,PERIOD_H8,PERIOD_H12};

//--- indicator buffers
double Buffer1[];

//datetime time_alert; //used when sending alert
datetime time_alert[27,21];
datetime test;
extern bool Audible_Alerts=true;
double myPoint; //initialized in OnInit
//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
void myAlert(string type,string message, string symbol, int period)
  {
  

   if(type=="print")
      Print(message);
   else if(type=="error")
     {
      Print(type+" | GeneralDailyAlert @ "+symbol+","+period+" | "+message);
     }
   else if(type=="order")
     {
     }
   else if(type=="modify")
     {
     }
   else if(type=="indicator")
     {
      Print(type+" | GeneralDailyAlert @ "+symbol+","+period+" | "+message);
      if(Audible_Alerts) Alert(type+" | GeneralDailyAlert @ "+symbol+","+period+" | "+message);
     }
  }
//+------------------------------------------------------------------+
//| Custom indicator initialization function                         |
//+------------------------------------------------------------------+
int OnInit()
  {
   IndicatorBuffers(1);
   SetIndexBuffer(0,Buffer1);
   SetIndexEmptyValue(0,0);
   SetIndexArrow(0,67);
//initialize myPoint
   myPoint=Point();
   if(Digits()==5 || Digits()==3)
     {
      myPoint*=10;
     }
   return(INIT_SUCCEEDED);
  }
//+------------------------------------------------------------------+
//| Custom indicator iteration function                              |
//+------------------------------------------------------------------+
int OnCalculate(const int rates_total,
                const int prev_calculated,
                const datetime &time[],
                const double &open[],
                const double &high[],
                const double &low[],
                const double &close[],
                const long &tick_volume[],
                const long &volume[],
                const int &spread[])
  {
  
   int limit=rates_total-prev_calculated;
//--- counting from 0 to rates_total
   ArraySetAsSeries(Buffer1,true);
//--- initial zero
   if(prev_calculated<1)
     {
      ArrayInitialize(Buffer1,0);
     }
   else
      limit++;

// Loop for Currency pairs inside CurrPair array
   for(int j=0;j<ArraySize(CurrPair);j++)
     {

      // Loop for all time frames
      for(int z=0; z<ArraySize(timeFrames);z++)
        {

         // Loop for the bars for the given currency pair
         for(int i=limit-1; i>=0; i--)
           {


            if(i>=MathMin(5000-1,rates_total-1-50)) continue; //omit some old rates to prevent "Array out of range" or slow calculation   
                                                              //Indicator Buffer 1
            if((iHigh(CurrPair[j],timeFrames[z],i)-iLow(CurrPair[j],timeFrames[z],i))>iATR(CurrPair[j],PERIOD_D1,1,i)
               && (iHigh(CurrPair[j],timeFrames[z],i+1)-iLow(CurrPair[j],timeFrames[z],i+1))<iATR(CurrPair[j],PERIOD_D1,1,i+1) //Candlestick Range crosses above Average True Range
               )
              {
               ///////////////////////////////////////////////////////////////////////////
               //Print("Entered First Condition for currency pair: "+CurrPair[j] + i);
               ///////////////////////////////////////////////////////////////////////////

               Buffer1[i]=iLow(CurrPair[j],timeFrames[z],i)-4*myPoint; //Set indicator value at Candlestick Low - fixed value
               if(i==1 && iTime(CurrPair[j],timeFrames[z],1)!=time_alert[j,z])
                 {
                  // indicator, alerts, symbol, period
                  myAlert("indicator","Alert",CurrPair[j],timeFrames[z]); //Alert on next bar open
                 }
               time_alert[j,z]=iTime(CurrPair[j],timeFrames[z],1);

              }
            else
              {
               Buffer1[i]=0;
              }
           }
        }
     }
   return(rates_total);
  }
//+------------------------------------------------------------------+
