**First Attempt**

Solution Domain:
---

The challenge in the problem is the circular motion and finding the the distance between two point as movement happens. For instance, if you have 5 trees in the garden (1,2,3,4,5) and the monkey start from point '1', the distance between 1 – 2 and 1 – 5 is same (1 Unit) and the distance between 1 - 3 and 1 – 4 is again same (2 Unit) . It means the minimum distance to reach point 4 from 1 is 2 Unit (1 – 5 – 4) rather than 4 Units (1 – 2 – 3 – 4). The case will be true for all the points. The solution need to traverse half of the total data which will result in covering the complete circle data. The maximum distance will require us to iterate through the trees height and distance on the way. The recored data, as we traverse, is stored in a hash table. We then iterate over the hash table to find the maximum value, which will be the maximum travelling time between the monkeys.

Bug
---

The proposed solution will fail in conditions when we have multiple trees of same height.

**Yadav, Anil (Coppin State University)