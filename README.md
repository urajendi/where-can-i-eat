# where-can-i-eat

## Goal: Write a set of functions that provide a list of food trucks using the provided url to fetch food truck data and given timestamp.

1. Fetch data from given URL.
2. Convert the unix timestamp given to extract day, time (UTC format).
3. Use above values to filter food truck data to list food trucks open at the given time and day.
4. If no matches are found return N/A

## Input: First element is URL for fetching food truck data. Second element is unix timestamp to be used to extract day and time (UTC format). DayOrder represents day of week in integer (0 represents Sunday).

## Structure of JSON data is array of objects as given below:
[{
      "DayOrder":2,
      "DayOfWeekStr":"Tuesday",
      "starttime":"10AM",
      "endtime":"6PM",
      "permit":"19MFF-00105",
      "PermitLocation":"773 MARKET ST",
      "locationdesc":"Pushcart located on Market St. 7 linear feet West of the Fire Hydrant. Must maintain 8 linear feet clearance from Street Artist Booth M22. Reference Street Artist Map #14 (http:\/\/www.sfartscommission.org\/street_artists_program\/maps\/index.html)",
      "optionaltext":"Kettle Corn, Funnel Cakes, Lemonade, Beverages, Flan, Hot Dogs, Falafel, Hot and Cold Sandwiches, French Fries, Baklava and Pastries",
      "locationid":1341056,
      "scheduleid":null,
      "start24":"10:00",
      "end24":"18:00",
      "CNN":8746103,
      "Addr_Date_Create":"11\/15\/2011 01:48:04 PM",
      "Addr_Date_Modified":"11\/15\/2011 01:50:08 PM",
      "block":"3706",
      "lot":"096",
      "ColdTruck":"N",
      "Applicant":"Kettle Corn Star",
      "X":"6,011,164.82111",
      "Y":"2,114,324.40143",
      "Latitude":37.7861609344,
      "Longitude":-122.4051273113,
      "Location":"(37.7861609344287, -122.405127311306)"
   }, ...]

## Output: It must match the provided "Sample Output" format with no quotes, additional leading spaces, or trailing spaces. It should be a list of food truck names that are open at the time and date provided in form of the unix timestamp in alphabetical order.

For example, if its Friday May 5 at 12pm, then I should only see food trucks that are open then.
If no matches are found return N/A

# Explanation

Please find the explanation in the PDF named 'explanation'