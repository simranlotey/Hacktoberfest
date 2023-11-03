// write program to convert string into SHA-256 hash code

import * as crypto from "crypto"

function calculateSHA256Hash(data: string): string {
  // Create a hash object
  const sha256Hash = crypto.createHash("sha256")

  // Update the hash with the data
  sha256Hash.update(data, "utf8")

  // hexadecimal representation of the hash
  const hashHex: string = sha256Hash.digest("hex")

  return hashHex
}

const data: string = "Hello World"
const hash: string = calculateSHA256Hash(data)

console.log("SHA-256 Hash:", hash)
