import math

annual_demand = 12000 # units per year
setup_cost = 50 # cost per production run, in Rand
holding_cost = 2 # cost per unit per year, in Rand
daily_demand_rate = 40 # units produced/sold per day
daily_production_rate = 150 # units your process can make per day

def calculate_epq(demand, setup, hold_cost, d_rate, p_rate):
 return math.sqrt((2 * demand * setup) / (hold_cost * (1 - d_rate / p_rate)))
epq = calculate_epq(annual_demand, setup_cost, holding_cost,
 daily_demand_rate, daily_production_rate)
print("Optimal production quantity:", round(epq, 2))

runs_per_year = annual_demand / epq
run_length_days = epq / daily_production_rate
print("Production runs per year:", round(runs_per_year, 2))
print("Length of each run (days):", round(run_length_days, 1))

max_inventory = epq * (1 - daily_demand_rate / daily_production_rate)
print("Maximum inventory level:", round(max_inventory, 2))
# The EPQ goes down , because we are producing at a rate faster than the demand, which means we can produce less per run and still meet the demand. The maximum inventory level is also lower because we are not holding as much inventory at any given time.
#As the production rate becomes much larger than the demand rate, inventory is replenished almost instantaneously. Therefore, the EPQ production process behaves like the instantaneous replenishment assumption of EOQ, making the EPQ and EOQ values nearly identical.