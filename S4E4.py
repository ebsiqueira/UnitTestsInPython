def max_min_diff(numbers):
    assert len(numbers) != 0, 'The numbers object cannot be empty.'
    return max(numbers) - min(numbers)
    
# enter your solution here
if __name__ == '__main__':
    max_min_diff([])