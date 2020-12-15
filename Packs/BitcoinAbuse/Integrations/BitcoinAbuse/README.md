This is integration for Bitcoin Abuse API. contains 2 commands, bitcoin-report-address and fetch-indicators
This integration was integrated and tested with version xx of BitcoinAbuse.
Supported Cortex XSOAR versions: 5.0.0 and later.

## Configure BitcoinAbuse on Cortex XSOAR

1. Navigate to **Settings** > **Integrations** > **Servers & Services**.
2. Search for BitcoinAbuse.
3. Click **Add instance** to create and configure a new integration instance.

    | **Parameter** | **Description** | **Required** |
    | --- | --- | --- |
    | incidentType | Incident type | False |
    | api_key | API Key | True |
    | insecure | Trust any certificate \(not secure\) | False |
    | proxy | Use system proxy settings | False |
    | feedIncremental | Incremental Feed | False |
    | feed | Fetch indicators | False |
    | feedReputation | Indicator Reputation | False |
    | feedReliability | Source Reliability | True |
    | feedExpirationPolicy |  | False |

4. Click **Test** to validate the URLs, token, and connection.
## Commands
You can execute these commands from the Cortex XSOAR CLI, as part of an automation, or in a playbook.
After you successfully execute a command, a DBot message appears in the War Room with the command details.
### fetch-indicators
***
 


#### Base Command

`fetch-indicators`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |


#### Context Output

There is no context output for this command.

#### Command Example
``` ```

#### Human Readable Output

### fetch-indicators
***

### bitcoin-report-address
***
Reports an abuser to Bitcoin Abuse API. abuse_type_other field is required when abuse_type is other


#### Base Command

`bitcoin-report-address`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| address | address of the abuser. | Required | 
| abuser | information of the abuser. | Required | 
| description | description of the abusement. | Optional | 
| abuse_type | type of abuse made. abuse_type_other field is required when abuse_type is other . Possible values are: ransomware, darknet market, bitcoin tumbler, blackmail scam, sextortion, other. | Required | 
| abuse_type_other | description of abuse type, abuse_type_other field is required when abuse_type is other. | Optional | 


#### Context Output

There is no context output for this command.

#### Command Example
```!bitcoin-report-address address=1FTJfkSLXj3JoWpW2ZKjk7FdWcTepWGQUC abuser=abuser@abuse.net abuse_type="bitcoin tumbler" description="this is a description of the abuse"```

#### Context Example
```json
{}
```

#### Human Readable Output

>bitcoin address 1FTJfkSLXj3JoWpW2ZKjk7FdWcTepWGQUC by abuser abuser@abuse.net was reported to BitcoinAbuse API
