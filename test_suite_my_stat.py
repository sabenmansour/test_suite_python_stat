import unittest
from MyOwnStats import *
from random import randint
import numpy as np

class TestMyOwnStats(unittest.TestCase):

	def setUp(self):
		# Set up any data or configuration needed for your tests here.
		pass

	def tearDown(self):
		# Clean up after each test if necessary.
		pass

	def test_min(self):
		data = [10, 5, 42, 2, 7]
		self.assertEqual(Min(data), 2)

	def test_max(self):
		data = [10, 5, 42, 2, 7]
		self.assertEqual(Max(data), 42)

	def test_cardinality(self):
		data = [10, 5, 42, 2, 7]
		self.assertEqual(Cardinality(data), 5)

	def test_mean(self):
		# Test the Mean function
		distribution = (10, 5, 42)  # Sample distribution
		expected_mean = (10 + 5 + 42) / 3  # Expected mean

		# Calculate the mean using your function
		actual_mean = Mean(distribution)

		# Check if the actual mean matches the expected mean
		self.assertEqual(actual_mean, expected_mean)

	def test_generate_distribution(self):
		# Test GenerateDistribution function
		n = random.randint(1, 18) #We start from 1 bcs 0 => error for min/max test
		distribution_0 = GenerateDistribution(0)
		distribution_10 = GenerateDistribution(10)
		distribution_n = GenerateDistribution(n)
		self.assertEqual(len(distribution_0[2]), 0)
		self.assertEqual(len(distribution_10[2]), 10)
		self.assertEqual(len(distribution_10[2]), 10)
		self.assertEqual(distribution_0[0], 0)
		self.assertEqual(distribution_10[0], min(distribution_10[2]))
		self.assertEqual(distribution_n[0], min(distribution_n[2]))
		self.assertEqual(distribution_0[1], 0)
		self.assertEqual(distribution_10[1], max(distribution_10[2]))
		self.assertEqual(distribution_n[1], max(distribution_n[2]))


	def test_sort_distribution(self):
		# Test SortDistribution function
		distribution = (3, 1, 2)
		sorted_asc = SortDistribution(distribution)
		sorted_desc = SortDistribution(distribution, asc=False)
		self.assertEqual(sorted_asc, (1, 2, 3))
		self.assertEqual(sorted_desc, (3, 2, 1))

	def test_add_value_distribution(self):
		# Test AddValueDistribution function
		distribution = (1, 2, 3)
		new_distribution = AddValueDistribution(distribution, 4)
		self.assertEqual(new_distribution, (1, 2, 3, 4))
		with self.assertRaises(ValueNotInteger):
			AddValueDistribution(distribution, "not_an_integer")

	def test_add_value_position_distribution(self):
		# Test AddValuePositionDistribution function
		distribution = (1, 2, 3)
		new_distribution = AddValuePositionDistribution(distribution, 4, 1)
		self.assertEqual(new_distribution, (1, 4, 2, 3))
		with self.assertRaises(ValueNotInteger):
			AddValuePositionDistribution(distribution, "not_an_integer", 1)

	def test_delete_value_distribution(self):
		# Test DeleteValueDistribution function
		distribution = (1, 2, 3, 2)
		new_distribution = DeleteValueDistribution(distribution, 2)
		self.assertEqual(new_distribution, (1, 3, 2))
		with self.assertRaises(ValueNotInteger):
			DeleteValueDistribution(distribution, "not_an_integer")
		with self.assertRaises(ValueNotFoundInDistribution):
			DeleteValueDistribution(distribution, 4)
		with self.assertRaises(DistributionEmpty):
			DeleteValueDistribution((), 1)

	def test_delete_position_distribution(self):
		# Test DeletePositionDistribution function
		distribution = (1, 2, 3)
		new_distribution = DeletePositionDistribution(distribution, 1)
		self.assertEqual(new_distribution, (1, 3))
		with self.assertRaises(DistributionEmpty):
			DeletePositionDistribution((), 1)

	def test_merge_distribution(self):
		# Test MergeDistribution function
		distribution1 = (1, 2, 3)
		distribution2 = (4, 5, 6)
		merged_distribution = MergeDistribution(distribution1, distribution2)
		self.assertEqual(merged_distribution, (1, 2, 3, 4, 5, 6))

	def test_standardDeviation(self):
		pass
if __name__ == '__main__':
	unittest.main()

