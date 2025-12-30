import time

class CollatzDualStream:
    """
    A Pseudo-Random Number Generator (PRNG) based on the chaotic nature of 
    two coupled Collatz (3n+1) streams.
    
    Architecture:
    - Maintains two internal states: stream_a and stream_b.
    - Evolves both using the Collatz rule.
    - Couples them via XOR to induce non-linear dependency.
    - Extracts entropy from the race condition (comparator) between states.
    """
    
    def __init__(self, seed: int):
        """
        Initialize the Dual Motors using a split of the master seed.
        """
        if not isinstance(seed, int):
            raise ValueError("Seed must be an integer.")
            
        # Architecture: Split Seed
        # Stream A takes the raw seed
        self.stream_a = seed
        
        # Stream B takes a mutated version to ensure divergence at t=0
        # We use a bitwise inversion and an arbitrary salt (0xA5A5A5A5)
        # to ensure stream_b starts differently even for small seeds.
        self.stream_b = (~seed) ^ 0xA5A5A5A5
        
        # Ensure positive integers for Collatz (traditional domain)
        self.stream_a = abs(self.stream_a) if self.stream_a != 0 else 1
        self.stream_b = abs(self.stream_b) if self.stream_b != 0 else 1
        
        self.step_count = 0

    def _collatz_rule(self, n: int) -> int:
        """Applies one step of the Collatz map."""
        if n % 2 == 0:
            return n // 2
        else:
            return 3 * n + 1

    def _advance_state(self) -> int:
        """
        Advances the state of both streams and returns a single bit.
        
        Cycle:
        1. Apply Collatz to A.
        2. Apply Collatz to B.
        3. Fracture: A = A XOR B (Coupling).
        4. Emit: 1 if A > B else 0.
        """
        # 1. Dual Motor Execution
        next_a = self._collatz_rule(self.stream_a)
        next_b = self._collatz_rule(self.stream_b)
        
        # 2. Coupling (The Twist)
        # The streams are not independent; A is contaminated by B's state.
        self.stream_a = next_a ^ next_b
        self.stream_b = next_b # B evolves naturally this step, but influences A
        
        self.step_count += 1
        
        # 3. Bit Generation from Relative State
        return 1 if self.stream_a > self.stream_b else 0

    def generate_32bit_string(self) -> str:
        """
        Generates a 32-bit binary string by advancing the coupled streams.
        """
        bits = ""
        for _ in range(32):
            bits += str(self._advance_state())
        return bits

    def __str__(self):
        """
        Visualizes the 'Race' between the streams for a demo period (5 steps),
        then resets the generator to initial state for fairness if actual generation follows.
        
        Note: This is a state-modifying preview, but we restore state for consistency 
        if this method is just for show. Implementation chops: High.
        """
        # Snapshot current state to restore after demo
        saved_a, saved_b, saved_step = self.stream_a, self.stream_b, self.step_count
        
        output = []
        output.append("=== Collatz DualStream Architecture Demo ===")
        output.append(f"{'Step':<6} | {'Stream A':<20} | {'Stream B':<20} | {'Coupling (A^B)':<15} | {'Bit'}")
        output.append("-" * 80)
        
        for i in range(1, 6):
            # Capture state before step
            prev_a = self.stream_a
            prev_b = self.stream_b
            
            # Calculate next standard Collatz (pre-coupling) for display logic
            col_a = self._collatz_rule(prev_a)
            col_b = self._collatz_rule(prev_b)
            
            # Execute actual step
            bit = self._advance_state()
            
            # Visuals
            output.append(
                f"#{i:<5} | {prev_a:<7} -> {col_a:<8} | {prev_b:<7} -> {col_b:<8} | {self.stream_a:<15} | {bit}"
            )
            
        output.append("-" * 80)
        output.append("...Streams Coupled. Entropy accumulating...")
        
        # Restore state so calling print(gen) doesn't consume entropy
        self.stream_a = saved_a
        self.stream_b = saved_b
        self.step_count = saved_step
        
        return "\n".join(output)

if __name__ == "__main__":
    try:
        # Prompt for user input
        user_input = input("Enter an integer seed to start the generator: ")
        seed_input = int(user_input)
    except ValueError:
        print("Invalid input! Using system time as fallback.")
        seed_input = int(time.time() * 1000)

    prng = CollatzDualStream(seed_input)
    
    print(f"\nInitialized with seed: {seed_input}\n")
    
    # Show the flashy demo string
    print(prng)
    
    # Generate actual requested output
    result = prng.generate_32bit_string()
    print(f"\n[OUTPUT] 32-Bit Generated Sequence:")
    print(f"> {result}")
