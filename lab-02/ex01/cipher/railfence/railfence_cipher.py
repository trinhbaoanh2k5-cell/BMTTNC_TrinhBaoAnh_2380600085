class RailFenceCipher:
    def rail_fence_encrypt(self, plain_text, num_rails):
        fence = [['\n' for _ in range(len(plain_text))] for _ in range(num_rails)]
        rail = 0
        direction = 1
        for i in range(len(plain_text)):
            fence[rail][i] = plain_text[i]
            rail += direction
            if rail == 0 or rail == num_rails - 1:
                direction *= -1
        
        encrypted_text = "".join(["".join([c for c in rail if c != '\n']) for rail in fence])
        return encrypted_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        fence = [['\n' for _ in range(len(cipher_text))] for _ in range(num_rails)]
        rail = 0
        direction = 1
        for i in range(len(cipher_text)):
            fence[rail][i] = '*'
            rail += direction
            if rail == 0 or rail == num_rails - 1:
                direction *= -1
        
        index = 0
        for i in range(num_rails):
            for j in range(len(cipher_text)):
                if fence[i][j] == '*' and index < len(cipher_text):
                    fence[i][j] = cipher_text[index]
                    index += 1
        
        result = []
        rail = 0
        direction = 1
        for i in range(len(cipher_text)):
            result.append(fence[rail][i])
            rail += direction
            if rail == 0 or rail == num_rails - 1:
                direction *= -1
        return "".join(result)