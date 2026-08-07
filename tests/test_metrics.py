from simulation.metrics import Metrics

m = Metrics()

m.add_success(120)
m.add_success(150)
m.add_failure()

print(m.total)
print(m.success)
print(m.failed)

print(m.average_latency())
print(m.success_rate())