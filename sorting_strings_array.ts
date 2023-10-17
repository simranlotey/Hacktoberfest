function sortStringsArray(arr: string[]): string[] {
    let res: string[] = Object.assign([], arr);
    return res.sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
}