
# Download de arquivos de videos 

Esse repo e publico mas foi construido com o intuido particular de transferencia de alguns arquivos de um computador local para um servidor na nuvem utilizando ngrok e o laravel como fornecedores de acesso aos links dos arquivos e a um json

### Versão Python
```bash
    Python 3.7.16
```
### Requesitos
```bash
pip install fastdownload
```

## Função Fornecedora do Json

Essa função e utilizada para fornecer um json com os caminhos a serem utilizados, pastas, subpastas, arquivos

#### Função PHP
```php
    function listFiles($dir_path){
        $rdi = new \RecursiveDirectoryIterator($dir_path);

        $rii = new \RecursiveIteratorIterator($rdi);
    
        $tree = [];
    
        foreach ($rii as $splFileInfo) {
            $file_name = $splFileInfo->getFilename();
    
            // Skip hidden files and directories.
            if ($file_name[0] === '.') {
                continue;
            }
    
            $path = $splFileInfo->isDir() ? array($file_name => array()) : array($file_name);
    
            for ($depth = $rii->getDepth() - 1; $depth >= 0; $depth--) {
                $path = array($rii->getSubIterator($depth)->current()->getFilename() => $path);
            }
    
            $tree = array_merge_recursive($tree, $path);
        }
    
        return $tree;
    }
```
#### Utilização da função

```php
json_encode([
    "NOMEANDO_SAIDA_1"=>$this->listFiles('folder_a_ser_localizada'),
    "NOMEANDO_SAIDA_2"=>$this->listFiles('folder_a_ser_localizada')
    ])
```
Foi utilizado o laravel para fornecer acesso aos arquivos e baixalos, função do controller laravel para download


#### Resposta em Json

```json
{
    "NOMEANDO_SAIDA_1": {
        "PASTA": {
            "SUB-PASTA": {
                "SUB-SUB-PASTA": [
                    "FILE.MP4",
                    "FILE.key",
                    "FILE.TXT",
                    "FILE.CSV"
                ]
            },
            "SUB-PASTA-1": {
                "SUB-SUB-PASTA": [
                    "FILE.MP4",
                    "FILE.key",
                    "FILE.TXT",
                    "FILE.CSV"
                ]
            }
        }
    }
}
```


#### Função download laravel
```php
public function downloadFiles($_PARAMETROS_DE_ONDE_OS_ARQUIVOS_SE_ENCONTRAM)
    {
        return Storage::disk($_DRIVE_)->download("{__PASTAS_DE_ONDE_SE_ENCONTRAM_OS_ARQUIVOS__}/{$__ARQUIVO_}");
    }
```
