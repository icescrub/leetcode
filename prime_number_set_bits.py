Why no is_prime definition? Because L,R only get as big as 10^6, which is ~ 2^20, so 20 bits that could be prime. Primes below 20 are below...

class Solution:
    def countPrimeSetBits(self, L, R):
        num_primes = 0
        
        for n in range(L,R+1):
            set_bits = [x for x in bin(n)[2:]].count('1')
            if set_bits in [2,3,5,7,11,13,17,19]:
                num_primes += 1
            
        return num_primes
