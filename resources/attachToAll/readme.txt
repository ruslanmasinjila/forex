I found a workaround using a simple script. The script loops through all open charts and attaches the "template" of the indicator you sent me to each chart.
The template can be generated manually by first drag-and-dropping the indicator "Dailyrangealert.mq4" into any open chart, say "EURUSD" followed by "Chart->Template->Save Template".

Now copy the template file from the template folder into "MQL4->Files".

Last, put the script "attachToAll.mq4" into the scripts folder.
When the script is run, it will attach the indicator to all open charts.

I am sending you the following files
1. "attachToAll.mq4" (To be placed in the Scripts folder)
2. The Template file (.tpl) for  "Dailyrangealert.mq4" (To be placed inside ...\MQL4\Files )

Let me know if this is what you are looking for.


Regards,
Ruslan.