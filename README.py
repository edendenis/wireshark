#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar o `Wireshark` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar o `Wireshark` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _In this document are contained the main commands and settings to set up/install the `Wireshark` on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### `Wireshark`
# 
# O `Wireshark` é uma poderosa ferramenta de análise de protocolos de rede de código aberto, amplamente utilizada para capturar e inspecionar o tráfego de rede em tempo real. Ele permite que os usuários analisem pacotes de dados transmitidos por uma rede e fornece informações detalhadas sobre o tráfego, incluindo protocolos, origens e destinos de pacotes e seu conteúdo. O `Wireshark` é uma escolha valiosa para administradores de rede, engenheiros de segurança e profissionais de TI que precisam solucionar problemas de rede, diagnosticar problemas de desempenho e identificar possíveis ameaças de segurança. Sua interface de usuário robusta e recursos avançados o tornam uma ferramenta essencial para a análise de tráfego de rede em ambientes corporativos e de pesquisa.

# ## 1. Como configurar/instalar o `Wireshark` no `Linux Ubuntu` [1]
# 
# Para configurar/instalar o `Wireshark` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# Para configurar/instalar/usar o `Wireshark` no `Linux Ubuntu` através do `Terminal Emulator`, você pode seguir os seguintes passos:
# 
# 3. **Instale o `Wireshark`:** Após a atualização, instale o `Wireshark` usando o gerenciador de pacotes `apt`. Digite o seguinte comando no terminal: `sudo apt install wireshark -y`
# 
# 4. **Verifique se o Wireshark está instalado:** Antes de mais nada, confirme se o `Wireshark` foi realmente instalado. Você pode verificar isso executando: `wireshark --version`
# `
#     Se o `Wireshark` estiver instalado, esse comando retornará a versão instalada.
# 
# 5. **Crie o grupo `Wireshark`:** Se o `Wireshark` está instalado mas o grupo não existe, você pode criá-lo manualmente. Para isso, use o seguinte comando: `sudo groupadd wireshark`
# `
# 6. **Adicione o usuário ao grupo `Wireshark`:** Agora que o grupo existe, você pode adicionar seu usuário a ele com o comando que você tentou anteriormente: `sudo usermod -a -G wireshark edenedfsls`
# 
# 7. **Defina as permissões adequadas:** Para que os usuários do grupo `wireshark` possam capturar pacotes, é necessário ajustar as permissões do `dumpcap`, um componente do `Wireshark`. Execute os seguintes comandos:
#     
#     ```
#     sudo chgrp wireshark /usr/bin/dumpcap
#     sudo chmod 750 /usr/bin/dumpcap
#     sudo setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' /usr/bin/dumpcap
#     ```
# 
# 8. **Reinicie a sessão:** Após adicionar o usuário ao grupo `wireshark`, é necessário reiniciar a sessão (ou reiniciar o computador) para que as alterações entrem em vigor: `sudo systemclt reboot`
# 
# Essas etapas devem resolver o problema com a criação do grupo `wireshark` e permitir que você use o `Wireshark` para captura de pacotes sem precisar de privilégios de superusuário.

# ### 1.1 Código completo para configurar/instalar/usar
# 
# Para confiurar/instalar/usar o `Wireshark` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt clean
#     sudo apt autoclean
#     sudo apt autoremove -y
#     sudo apt update
#     sudo apt --fix-broken install
#     sudo apt clean
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     sudo apt install wireshark -y
#     wireshark --version
#     sudo groupadd wireshark
#     sudo chgrp wireshark /usr/bin/dumpcap
#     sudo chmod 750 /usr/bin/dumpcap
#     sudo setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' /usr/bin/dumpcap
#     # Reiniciar o computador
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***Instalar wireshark no ubuntu:*** Disponível em: <https://chatgpt.com/c/ecb19e97-055b-46be-8c2d-69c46534a754> (texto adaptado). Acessado em: 28/11/2023 16:02.
# 
# [2] OPENAI. ***Vs code: editor popular:*** https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42 (texto adaptado). Acessado em: 28/11/2023 16:02.
# 
