//+------------------------------------------------------------------+
//|                                                  attachToAll.mq4 |
//|                        Copyright 2019, MetaQuotes Software Corp. |
//|                                             https://www.mql5.com |
//+------------------------------------------------------------------+

#property copyright "Copyright 2019, MetaQuotes Software Corp."
#property link "https://www.mql5.com"
#property version "1.00"
#property strict
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart() {
 //---

 long chartID = ChartFirst();

 if (FileIsExist("Dailyrangealert.tpl")) {
  while (chartID >= 0) {
   
   bool addedToChart = ChartApplyTemplate(chartID, "Dailyrangealert.tpl");
   chartID = ChartNext(chartID);
   Print(addedToChart);
  }

 }

}

//+------------------------------------------------------------------+