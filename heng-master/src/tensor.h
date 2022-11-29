class tensor
{
private:
    float* data;
    int nElem;

public:
    tensor(int nElem);
    tensor* add(tensor *a);
    void show();
    ~tensor();
};
