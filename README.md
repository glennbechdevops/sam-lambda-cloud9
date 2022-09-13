# GitHub actions, AWS Lambda med API Gateway og AWS SAM

* I denne øvingen skal vi se på AWS SAM og hvordan vi kan deploye en AWS Lambdafunksjon.
  Vi skal også bruke AWS tjenesten "Comprehend" for å finne "stemningen" (Sentiment) i en tekst- og om den er negativt eller positivt
  ladet.

* Deployment og bygg skal gjøres med verktøyet "AWS SAM", vi skal senere sette dette i en pipeline med GitHub actions.

## Før dere starter

- Dere trenger en GitHub Konto
- Lag en _fork_ av dette repositoriet inn i din egen GitHub konto
* URL for innlogging er https://244530008913.signin.aws.amazon.com/console
* Brukernavnet og passordet er gitt i klasserommet
* Fra hovedmenyen, søk etter tjenesten "cloud9"

* Velg "your environments" fra venstremenyen hvis du ikke ser noen miljøer med ditt navn
* Hvis du ikke ser noe å trykke på som har ditt navn, pass på at du er i rett region (gitt i klasserommet)
* Velg "Open IDE"


Start en ny terminal i Cloud 9 ved å trykke (+) symbolet på tabbene
![Alt text](img/newtab.png  "a title")

### Klone din Fork (av dette repoet) inn i ditt Cloud 9 miljø

Fra terminalen i Cloud 9, lag en klone.

```shell
git clone https://github.com/≤github bruker>/02-lambda-sls-cd-only.git
```

## Test bygg kjør lambdafunkskonen med SAM fra Cloud 9

I cloud 9, åpne en Terminal

```shell
cd 02-lambda-sls-cd-only
cd sentiment-demo/
sam build --use-container
```

Dette vil ta litt tid første gangen du gjør operasjonen. Du kan teste funksjonen uten å deploye den til AWS
ved å kjøre kommandoen. Dette er veldig nyttig under utvikling når man ønsker så rask feedback som mulig.

```shell
sam local invoke -e event.json 
```

Event.json filen inneholder en request, nøyaktig slik API Gateway sender den til handler metoden/funksjonen.
Du skal få en respons omtrent som denne

```
{"statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": "{\"sentiment \": \"{\\\"Sentiment\\\": \\\"NEGATIVE\\\", \\\"SentimentScore\\\": {\\\"Positive\\\": 0.00023614335805177689, \\\"Negative\\\": 0.9974453449249268, \\\"Neutral\\\": 0.00039782875683158636, \\\"Mixed\\\": 0.0019206495489925146}, \\\"ResponseMetadata\\\": {\\\"RequestId\\\": \\\"c3367a61-ee05-4071-82d3-e3aed344f9af\\\", \\\"HTTPStatusCode\\\": 200, \\\"HTTPHeaders\\\": {\\\"x-amzn-requestid\\\": \\\"c3367a61-ee05-4071-82d3-e3aed344f9af\\\", \\\"content-type\\\": \\\"application/x-amz-json-1.1\\\", \\\"content-length\\\": \\\"168\\\", \\\"date\\\": \\\"Mon, 18 Apr 2022 12:00:06 GMT\\\"}, \\\"RetryAttempts\\\": 0}}\"}"}END RequestId: d37e4849-b175-4fa6-aa4b-0031af6f41a0
REPORT RequestId: d37e4849-b175-4fa6-aa4b-0031af6f41a0  Init Duration: 0.42 ms  Duration: 1674.95 ms    Billed Duration: 1675 ms        Memory Size: 128 MB     Max Memory Used: 128 MB
```

* Ta en ekstra kikk på event.json. Dette er objektet AWS Lambda får av tjenesten API Gateway .
* Forsøke å endre teksten i "Body" delen av event.json - klarer å å endre sentimentet til positivt ?

## Deploy med SAM fra Cloud 9

* Du kan også bruke SAM til å deploye lambdafunksjonen fra Cloud 9
* NB! Du må endre s3-prefix parameter name til noe unikt. Legg på ditt brukeranvn eller noe i slutten av navnet, for eksempel; ```--stack-name sam-sentiment-ola```

```shell
sam deploy --guided 
```

Dere får da et interaktivt UI, og må gjøre følgende valg, bytt ut "glennbech" med ditt egent navn

```text
     Setting default arguments for 'sam deploy'
        =========================================
        Stack Name [sam-sentiment-glennbech]: sam-sentiment-<ditt navn> 
        AWS Region [eu-west-1]: eu-west-1
        Parameter UnleashToken [12345]: <enter>
        #Shows you resources changes to be deployed and require a 'Y' to initiate deploy
        Confirm changes before deploy [Y/n]: Y
        #SAM needs permission to be able to create roles to connect to the resources in your template
        Allow SAM CLI IAM role creation [Y/n]: Y
        SentimentFunction may not have authorization defined, Is this okay? [y/N]: Y
        Save arguments to configuration file [Y/n]: Y
        SAM configuration file [samconfig.toml]: <enter>
        SAM configuration environment [default]: <enter> 
```

Du kan bruke for eksempel postman eller Curl til å teste ut tjenesten. <URL> får dere etter SAM deploy.

```shell
curl -X POST \
  <URL> \
  -H 'Content-Type: text/plain' \
  -H 'cache-control: no-cache' \
  -d 'The laptop would not boot up when I got it. It would let me get through a few steps of the setup process, then it would become unresponsive and eventually shut down, then restar, '
```

Men... dette er jo ikke veldig "DevOps" og vil ikke fungere i et større team. Vi trenger både CI og CD for å kunne jobbe
effektivt sammen om denne funksjonen.

## Ekstraoppgaver

* Bruk AWS lambda brukergrensesnitet til å lage en Lambda i et valgfritt språk
* Klarer du å lage en Javabasert Lambda ? 

