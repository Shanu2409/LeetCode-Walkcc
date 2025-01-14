class Solution {
 public:
  int maximumBeauty(vector<int>& nums, int k) {
    // l and r track max window instead of valid window.
    int l = 0;
    int r = 0;

    sort(nums.begin(), nums.end());

    for (r = 0; r < nums.size(); ++r)
      if (nums[r] - nums[l] > 2 * k)
        ++l;

    return r - l;
  }
};
