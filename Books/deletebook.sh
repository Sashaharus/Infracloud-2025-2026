APIKEY = ""
for BOOK in {900..910}
do
echo $BOOK
DELETE_url="http://library.demo.local/api/vl/books/"$BOOK
echo $DELETE_url
curl -X DELETE_url -H "accept: application/json" -H "X-API-KEY: $APIKEY" -H "content-Type: applecation/json"
done