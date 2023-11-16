
def count_batteries_by_health(present_capacities):
  healthy_count=0 #Here i took a counter to count the number of batteries of that are classified as healthy batteries
  exchange_count=0 #Here i took a counter to count the number of batteries of that are classified as exchange
  failed_count=0 #Here i took a counter to count the number of batteries of that are classified as failed

  for i in present_capacities:
    SoH_i=100 * i / 120  # SoH_i here means the SoH for the "i" in the present_capacities array.
    #  claculation of SoH ,SoH% = 100 * present_capacity / rated_capacity rated_capacity=120 as given
    if SoH_i>80 and SoH_i<=100:
        # SoH more than 80%, up to 100%: classified as healthy
        healthy_count+=1
    elif SoH_i<=80 and SoH_i>=62:
        #SoH between 80% and 62%: classified as exchange
      exchange_count+=1
    else:
        #SoH below 62%: classified as failed
      failed_count+=1
  return {
    "healthy": healthy_count,
    "exchange": exchange_count,
    "failed": failed_count
  }


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")
  # additional cases added
  print("Number of batteries given:",len(present_capacities)) #gives the number of total batteries
  print("Number of batteries that are healthy",counts["healthy"]) #gives the count of healthy batteries
  print("Number of batteries that are exhange",counts["exchange"])#gives the count of exchange batteries
  print("Number of batteries that are failed",counts["failed"])#gives the count of failed batteries

if __name__ == '__main__':
  test_bucketing_by_health()
