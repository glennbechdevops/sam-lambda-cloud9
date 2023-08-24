# GitHub actions, AWS Lambda med API Gateway og AWS SAM

* I denne øvingen skal vi se på AWS SAM og hvordan vi kan lage, bygge og deploye en AWS Lambdafunksjon.
* Deployment og bygg skal gjøres med verktøyet "AWS SAM", vi skal senere sette dette i en pipeline med GitHub actions.

## Før dere starter

* URL for innlogging er https://244530008913.signin.aws.amazon.com/console
* Brukernavnet og passordet er gitt i klasserommet
* Fra hovedmenyen, søk etter tjenesten "cloud9"

* Velg "your environments" fra venstremenyen hvis du ikke ser noen miljøer med ditt navn
* Hvis du ikke ser noe å trykke på som har ditt navn, pass på at du er i rett region (gitt i klasserommet)
* Velg "Open IDE"

Start en ny terminal i Cloud 9 ved å trykke (+) symbolet på tabbene
![Alt text](img/newtab.png  "a title")

## Test bygg kjør lambdafunkskonen med SAM fra Cloud 9

I cloud 9,åpne en Terminal

```shell
sam init
```

* Gjør egne valg, men videre i disse instrukskjonene antas det at du velger ```1 - Hello World Example``` og et valgfritt språk
* Gå inn i den opprettede prosjektmappen ved å bruke cd kommandoen.
* Bygg prosjektet med: ```sam build --use-container```
* Kjør Lambda lokalt med: ```sam local invoke FunctionName``` (bytt ut "FunctionName" med navnet på Lambda-funksjonen din).

## Deploy Lambda til AWS:

* Deploy Lambda ved å bruke: ```sam deploy --guided```
* OBS. Du trenger bare å bruke ```--guided``` flagget første gangen. SAM skriver en config fil i katalogen med valgene dine
og husker de til neste gang 

Her er et eksempel 

```text
     Setting default arguments for 'sam deploy'
        =========================================
        Stack Name [sam-sentiment-glennbech]: sam-demo-<ditt navn> 
        AWS Region [eu-west-1]: eu-west-1
        Confirm changes before deploy [Y/n]: Y
        #SAM needs permission to be able to create roles to connect to the resources in your template
        Allow SAM CLI IAM role creation [Y/n]: Y
        SentimentFunction may not have authorization defined, Is this okay? [y/N]: Y
        Save arguments to configuration file [Y/n]: Y
        SAM configuration file [samconfig.toml]: <enter>
        SAM configuration environment [default]: <enter> 
```

Nå skal Lambda-funksjonen din være deployet til AWS. Du kan få tilgang til Lambda i AWS Management Console under
Lambda-tjenesten. Test den derfra også.

Du vil få en output som inneholder en tekstblokk som ser omtrent slik ut

```text
Key                 HelloWorldApi                                                                                                                                 
Description         API Gateway endpoint URL for Prod stage for Hello World function                                                                              
Value               https://0bn59ws6tl.execute-api.eu-west-1.amazonaws.com/Prod/hello/      
```
Kopier URL fra Value i en nettleser for å sjekke at APIet ditt virker

Men... dette er jo ikke veldig "DevOps" og vil ikke fungere i et større team. Vi trenger både CI og CD for å kunne jobbe
effektivt sammen om denne funksjonen.


## Ekstraoppgaver

* Modifiser  lambda funksjonen - og gjør en ny sam build, og sam deploy.