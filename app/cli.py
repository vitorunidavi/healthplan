from domain.customer import Customer
def footer():
print('\n---')
print('Desenvolvido por: Vitor Hugo Tavares')


def create_customer():
name = input('Nome: ').strip()
dob_str = input('Data nascimento (YYYY-MM-DD): ').strip()
dob = date.fromisoformat(dob_str)
cid = _next_id['customer']
_next_id['customer'] += 1
c = Customer(id=cid, name=name, birth_date=dob)
_customers[cid] = c
logger.info(f'Cliente criado: {c}')


def create_plan():
name = input('Nome plano: ').strip()
base = float(input('Preço base: ').strip())
pid = _next_id['plan']
_next_id['plan'] += 1
p = Plan(id=pid, name=name, base_price=base, quota=config.get('default_quota'))
_plans[pid] = p
logger.info(f'Plano criado: {p}')


def list_plans():
for pid, p in _plans.items():
print(f"{pid}: {p.name} - R${p.base_price:.2f}")


def main_menu():
while True:
print('\n=== HealthPlan CLI ===')
print('1) Criar cliente')
print('2) Criar plano')
print('3) Listar planos')
print('0) Sair')
choice = input('> ').strip()
if choice == '1':
create_customer()
elif choice == '2':
create_plan()
elif choice == '3':
list_plans()
elif choice == '0':
footer()
break
else:
print('Opção inválida')


if __name__ == '__main__':
main_menu()
 
from factory.plan_factory import PlanFactory
from domain.customer import Customer
from domain.usage import Usage

def run_cli():
    print("\n=== Sistema de Planos de Saúde ===")

    name = input("Nome do cliente: ")
    age = int(input("Idade do cliente: "))
    plan_type = input("Tipo de plano (basico/plus/premium): ").lower()

    factory = PlanFactory()
    plan = factory.create(plan_type)

    customer = Customer(name=name, age=age, plan=plan)

    print(f"\nPlano selecionado: {plan.name}")
    print(f"Preço base: R${plan.base_price:.2f}")

    use = input("Deseja registrar algum uso? (s/n): ")
    if use == "s":
        desc = input("Descrição do uso: ")
        amount = float(input("Valor do uso: "))
        usage = Usage(description=desc, amount=amount)
        plan.apply_usage(usage)

    final_price = plan.calculate_price(customer.age)

    print(f"\nPreço final após cálculos: R${final_price:.2f}")
if __name__ == "__main__":
    run_cli()
