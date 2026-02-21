### Beedude 2 - Bee Solutions ✅ ###
--- ---
# Projeto destinado a criação de mapas de rede (Integrado ao Zabbix via API)

- Sobre o projeto:
> - Desenvolvido por: Bee Solutions
> - Autor: Fernando Almondes
> - Principais Ferramentas: Cytoscape.js, Htmx, Python, Django e Zabbix
--- ---

- Distribuições homologados (Sistemas Operacionais Linux Server)
> - Debian 12 e Debian 13
> - Zabbix 6.x e Zabbix 7.x
> - Python3.11
--- ---

- Funcionalidades do Beedude:
> - Criação de mapas com nodes e edges (Disponível ✅)
> - Indicadores para nodes e edges (Disponível ✅)
> - Integração com Zabbix via API (Disponível ✅)
> - Atualização em tempo real (Disponível ✅)
> - Labels customizaveis e com unidade (Disponível ✅)
> - Até 01 Mapa na versão Lite (Disponível ✅)
> - Painel de administração Django (Disponível ✅)
--- ---

# 1# Veja a apresentação no Youtube

[![Painel](https://beesolutions.com.br/static/home/images/bee/beedude2.png)](https://youtu.be/3ah-W4W3CdY)
--- ---

### Parte 0 - Mais informações sobre o Beedude ⚠️

- Antes de iniciar leia com atenção o nosso [Contrato de Licença de Uso (EULA) para o Beedude Lite](https://github.com/FernandoAlmondes/beedude-lite/blob/main/EULA.txt).
- A versão Lite do Beedude é limitado a somente 01 Mapa, não tente criar múltiplos mapas, isso só vai fazer a api parar de atualizar. '-'
- Caso precise de múltiplos mapas contrate uma licença comercial [Bee Solutions](https://beesolutions.com.br).

--- ---

- Com o Beedude você pode criar mapas de redes e integrar com indicadores do Zabbix para métricas e triggers para status e alertas;
- O Beedude suporta múltiplos mapas e é possível integrar com diferentes servidores Zabbix;
- O Beedude usa cache para manter os dados atualizados e disponíveis de maneira rápida e leve;
- A topopoliga é separada do estado, então você pode criar toda a sua topologia e depois ir "animando" com itens e triggers do Zabbix;
- Macros são suportadas nas labels para calcular unidade e customizar o texto, por exemplo:
> - Bits in: {{1234}} {{lastvalue}} {{bps}} -> Bits in: 1.5gbps
> - Bits out: {{4321}} {{lastvalue}} {{bps}} -> Bits out: 8.5gbps
> - CPU: {{1234}} {{lastvalue}} {{%}} -> CPU: 50%
- Valores disponíveis: ['itemid', 'lastclock', 'prevvalue', 'lastclock_dt'...]
- Você pode criar nodes com diferentes ícones, router, server, nuvem e etc;
- Você também pode criar nodes com classes do tipo marcador (ponto), label (label customizada) ou nota (nota sobre o node ou label).

- Comparativo de versões do Beedude:

| Funcionalidade | Beedude Lite  | Beedude Pro  |
| :---:          | :---:         | :---:        |
| Mapas          | 01 mapa       | Sob demanda  |
| Gráficos       | ❌            | ✅          |
| Export/Import  | ❌            | ✅          |
| Suporte        | ❌            | ✅          |

# Instalação do Beedude #
--- ---

- Logue como root no servidor Debian 12 ou Debian 13.
```shell
su -
```

- Crie o diretorio base para o projeto (Bee).
```shell
mkdir -p /opt/bee/
```

- Navegue até o diretorio base do projeto.
```shell
cd /opt/bee/
```

- Instale o git
```shell
apt update
apt -y install git
```

- Faça download do código fonte via Git.
```shell
git clone https://github.com/FernandoAlmondes/beedude-lite.git
```

- Ajuste o nome do diretorio.
```shell
mv beedude-lite beedude
```

- Entre no diretorio do projeto.
```shell
cd /opt/bee/beedude
```

- Ajustando as permissões do script de instalação do Beedude
```shell
chmod +x beedude-instalacao.sh
```

- Realizando a instalação do Beedude
```shell
./beedude-instalacao.sh
```

- Você pode acessar o Beedude pelo ip do seu servidor na porta 9000 (Credenciais padrões: beesoft / beesoft).
```shell
http://seu-ip:9000
```

- Acesse o admin e cadastre ou atualize o servidor padrão (Credenciais padrões: beesoft / beesoft).
```shell
http://seu-ip:9000/admin
```

- Para cadastrar o servidor você vai precisar de uma chave de API Zabbix
```shell
Zabbix -> Usuários -> Tokens da API
```

### Precisa de suporte adicional? ###
- [Contato Comercial](https://t.me/fernandoalmondes)

### Comunidade no Telegram e canal do YouTube ###

- [Comunidade no Telegram](https://t.me/beesolutions)
- [Canal no Youtuve](https://www.youtube.com/beesolutions)

> Participe e colabore com nossos projetos (Bee Solutions 2026).

### Participe do nosso Canal Pro e contribua com a comunidade ###

📌 Faça parte do canal exclusivo com conteúdos adicionais e atualizados em primeira mão. 📌

Valor da Assinatura: R$9,99

Opções de assinatura (Canal Bee Solutions Pro):

Opção 01 - Mercado Pago Mensal
https://www.mercadopago.com.br/subscriptions/checkout?preapproval_plan_id=2c9380848b2a4548018b2a8541d40010

Opção 02 - Mercado Pago Anual (Desconto de -17%)
https://www.mercadopago.com.br/subscriptions/checkout?preapproval_plan_id=2c9380848ca561bc018ca64caf210050

Opção 03 - Hotmart
https://hotm.io/beepromensal

Opção 04 - Hotmart Anual (Desconto de -17%)
https://hotm.io/beeproanual

Chave Pix (SOMENTE ASSINATURA ANUAL 📌):
dd93211c-c70a-4dae-a703-7c41836bc3fd

--- ---