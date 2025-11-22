# 📊 HealthPlan – Sistema de Análise de Saúde

Sistema desenvolvido em Python aplicando princípios avançados de Engenharia de Software, incluindo **Strategy**, **Factory Method**, **Decorator**, **Observer**, **Adapter** e **Singleton**, além de uma arquitetura organizada em módulos.  
Projeto desenvolvido por **Vitor Hugo Tavares**.

---

## 📁 Estrutura do Projeto

healthplan/
│
├── app/
│   └── main.py
│
├── domain/
│   ├── customer.py
│   ├── plan.py
│   ├── usage.py
│   └── __init__.py
│
├── strategies/
│   ├── age_pricing.py
│   ├── copay_pricing.py
│   └── coparticipation.py
│
├── decorators/
│   ├── base_rider.py
│   ├── dental_rider.py
│   ├── vision_rider.py
│   └── __init__.py
│
├── factory/
│   ├── plan_factory.py
│   └── __init__.py
│
├── observers/
│   ├── observer.py
│   └── __init__.py
│
├── adapter/
│   ├── usage_adapter.py
│   └── __init__.py
│
├── singleton/
│   ├── logger.py
│   └── __init__.py
│
├── tests/
│   ├── test_adapter.py
│   ├── test_decorator.py
│   ├── test_factory.py
│   ├── test_observer.py
│   ├── test_singleton.py
│   ├── test_strategy.py
│   └── dummy_classes.py
│
└── README.md

---

## 🧠 Padrões de Projeto Utilizados

### ✔ Strategy  
Utilizado para calcular valores de planos de saúde com base em diferentes políticas de precificação.

- **AgePricingStrategy** — preço por idade  
- **CopayPricingStrategy / CoparticipationPricing** — preço por coparticipação

---

### ✔ Factory Method  
Centraliza a criação de planos padronizados:

- `create_basic_plan()`
- `create_premium_plan()`
- `create_custom_plan()`

---

### ✔ Decorator  
Permite adicionar coberturas adicionais ao plano:

- **DentalRider**
- **VisionRider**

Cada rider adiciona custo extra ao plano base.

---

### ✔ Observer  
O objeto `Plan` notifica automaticamente observadores quando:

- a cota é consumida  
- a cota se aproxima do limite

O observador padrão utiliza o `Logger Singleton` para registrar avisos.

---

### ✔ Adapter  
Converte objetos externos de uso para o formato interno esperado pelo plano.

Exemplo:  
`DummyUsage` dos testes → `Usage`

---

### ✔ Singleton  
Garantia de uma única instância para:

- **Config**
- **Logger**

O logger armazena logs em memória (`logger.logs[]`) e é compartilhado entre todos os componentes.

---

## 🧪 Testes

Executar testes:

pytest -q

Resultado esperado:

14 passed in 0.17s

---

## ▶ Como Executar

1. Criar ambiente virtual:

python -m venv venv

2. Ativar:

Windows:
venv\Scripts\activate

3. Instalar pytest:

pip install pytest

4. Executar a aplicação:

python app/main.py

---

## 👤 Autor

Projeto desenvolvido por:

**Vitor Hugo Tavares**  
Estudante de Sistemas de Informação

---

## 📄 Licença

Uso acadêmico / educacional.
